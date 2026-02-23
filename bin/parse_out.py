import re

# The text you provided
noxim_summary = """
     5    2   7.61446        27      0.0816667           -1           83         664
     0   15   14.7222        29           0.08           -1           90         720
"""

def parse_noxim_output(text, x_dim=4):
    # 1. Isolate only the "detailed" array section to avoid routed_flits
    detailed_section = re.search(r"detailed = \[(.*?)\];", text, re.DOTALL)
    if not detailed_section:
        return {}, {}
    
    content = detailed_section.group(1)
    
    latency_map = {}
    hops_map = {}
    
    # 2. Extract: src, dst, avg_delay, max_delay
    # We look for lines starting with numbers, ignoring lines starting with %
    pattern = r"^\s+(\d+)\s+(\d+)\s+([\d\.]+)\s+(\d+)"
    matches = re.findall(pattern, content, re.MULTILINE)
    
    for src_s, dst_s, avg_s, max_s in matches:
        s, d = int(src_s), int(dst_s)
        avg_lat = float(avg_s)
        
        # Manhattan Hops Calculation
        h = abs(s % x_dim - d % x_dim) + abs(s // x_dim - d // x_dim)
        
        # Store results
        if s not in latency_map: latency_map[s] = {}
        latency_map[s][d] = {'avg_latency': avg_lat, 'max_latency': int(max_s)}
        
        if s not in hops_map: hops_map[s] = {}
        hops_map[s][d] = h

    return latency_map, hops_map

with open("./out/out.txt", "r") as f:
   log_data = f.read()

latencies, hops = parse_noxim_output(log_data)

print("Latency Dictionary:", latencies)
print("Hops Dictionary:", hops)