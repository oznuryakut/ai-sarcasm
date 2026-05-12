import os
import json

base_path = "model/sarkazm-model"  # checkpoint'lerin olduğu klasör

best_accuracy = 0
best_checkpoint = ""

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    trainer_file = os.path.join(folder_path, "trainer_state.json")

    if os.path.isfile(trainer_file):
        with open(trainer_file, "r") as f:
            trainer_state = json.load(f)
            logs = trainer_state.get("log_history", [])

            for log in logs:
                if "eval_accuracy" in log:
                    acc = log["eval_accuracy"]
                    if acc > best_accuracy:
                        best_accuracy = acc
                        best_checkpoint = folder

print(f"📌 EN YÜKSEK DOĞRULUK: {best_accuracy:.4f} → {best_checkpoint}")
