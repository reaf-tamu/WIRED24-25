# DONT FORGET TO STARTTHE HOST
# RUN THIS NEXT LINE IN A SEPERATE TERMINAL
# sudo docker run -it -p 9001:9001 roboflow/roboflow-inference-server-cpu


from inference_sdk import InferenceHTTPClient
import cv2
import time



# set up inference
client = InferenceHTTPClient(
    api_url="http://localhost:9001", # use local inference server
    api_key="Lw0LcAJ8WMWM4TKlD71v"
)



# function that prints out objects
def detect(result):
	# result is a weird object that combines lists and dictionaries
	if result and "output" in result[0]:
		output = result[0]["output"]
		predictions_data = output.get("predictions", {})
		predictions = predictions_data.get("predictions", [])
		
		# this can be used if you need to see what the variable options are
		# print(result[0])
	    
	    	# prints out every object that is detected
	    	# will look for just one in competition
		if predictions:
			for pred in predictions:
				x = pred["x"]
				class_name = pred["class"]
				print(f"Class: {class_name}, X: {x}")
		else:
			print("No predictions found in result.")
	else:
		print("No 'output' found in result.")
	print()	# give a blank line to seperate each image



# combine images into one to detect
def combine(frame):
	# Assume the frame contains the left and right images side by side
	height, width, _ = frame.shape
	half_width = width // 2

	# Split the image into left and right images
	left_image = frame[:, :half_width]
	right_image = frame[:, half_width:]

	# Create a combined image by overlaying (use blending or addWeighted)
	# Adjust alpha values to see both images
	alpha = 0.5  # Transparency factor
	combined_image = cv2.addWeighted(left_image, alpha, right_image, 1 - alpha, 0)
	
	return combined_image
		
		

#camera
cam = cv2.VideoCapture(0)


# get result in real time
while True:
	info, image = cam.read(0)
	combined_image = combine(image)
	

	result = client.run_workflow(
	    workspace_name="bouy-detector",
	    workflow_id="detect-and-classify",
	    images={
		"image": combined_image
	    }
	)

	detect(result)
	time.sleep(1)
    

