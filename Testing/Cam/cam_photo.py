from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="http://localhost:9001", # use local inference server
    api_key="Lw0LcAJ8WMWM4TKlD71v"
)

result = client.run_workflow(
    workspace_name="bouy-detector",
    workflow_id="detect-and-classify",
    images={
        "image": "red.jpg"
    }
)

print(result[0])

if result and "output" in result[0]:
    output = result[0]["output"]
    predictions_data = output.get("predictions", {})
    predictions = predictions_data.get("predictions", [])
    
    if predictions:
        for pred in predictions:
            x = pred["x"]
            class_name = pred["class"]
            print(f"Class: {class_name}, X: {x}")
    else:
        print("No predictions found in result.")
else:
    print("No 'output' found in result.")

"""
predictions = result[0]["detection_predictions"]["predictions"]

print(predictions)
"""
