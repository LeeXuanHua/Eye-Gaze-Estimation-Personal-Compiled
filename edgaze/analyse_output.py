import glob
import re

total_time_pattern = re.compile(r"Inferred gaze in (.*)")
frame_count_pattern = re.compile(r"Infer openEDS/S_\S+ \(\d+\/(\d+)\)")

output_map = {}
log_list = [file.replace("\\", "/") for file in glob.glob('./**/*.log', recursive=True)]

for filepath in log_list:
    with open(filepath, "r") as f:
        content = f.read()

        total_time = float(re.search(total_time_pattern, content).group(1))
        frame_count = int(re.search(frame_count_pattern, content).group(1))
        avg_time = total_time / frame_count

        output_map[filepath.split("/")[1]] = [frame_count, total_time, avg_time]

with open("comparison.csv", "w") as f:
    f.write("model,mode,threshold,frame_count,total_time,avg_time\n")
    for key, value in output_map.items():
        model = key.rsplit("_", 2)[-3].split("_", 1)[-1]
        mode = key.rsplit("_", 2)[-2]
        threshold = key.rsplit("_", 1)[-1]
        f.write(f"{model},{mode},{threshold},{value[0]},{value[1]},{value[2]}\n")