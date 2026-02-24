from noc_transfer import *
import paths
import consts
import math

def write_noxim_table(transfer_list, filename):
    with open(filename, "w") as f:
        f.write(f"# {'src':<5} {'dst':<5} {'cycle':<10} {'size':<10}\n")
        f.write("# ------------------------------------------\n")
        
        for trans in transfer_list:
            trans : NocTransfer
            for entry in trans.generate_table_entries():
                line = f"{entry['src']:<7} {entry['dst']:<7} {entry['cycle']:<10} {entry['size']:<10}\n"
                f.write(line)
    
    print(f"Success: {filename} generated with {sum(len(t.dst_ids) for t in transfer_list)} potential entries.")

# --- Define Test Scenario ---
if __name__ == "__main__":
    # Test 1: A 1-to-1 transfer (e.g., Control signal)
    transfer1 = NocTransfer(src_id=0, dst_ids=15, 
                            size=int(math.ceil(64 * 8192 / consts.FLIT_SIZE)),
                              start_cycle=10)

    # Test 2: DRAM "All-Read" Broadcast from Hub 0 Gateway (Node 0)
    # Target: All other nodes in the Hub 0 quadrant
    transfer2 = NocTransfer(src_id=0, dst_ids=[1, 4, 5], 
                            size=int(math.ceil(64 * 4096 / consts.FLIT_SIZE)),
                            start_cycle=100)

    # Test 3: DRAM "All-Read" Broadcast from Hub 3 Gateway (Node 15)
    # Target: All other nodes in the Hub 3 quadrant
    transfer3 = NocTransfer(src_id=15, dst_ids=[10, 11, 14], 
                            size=int(math.ceil(64 * 4096 / consts.FLIT_SIZE)), 
                            start_cycle=100)

    # Compile and Write
    table_file_name = 'tst.txt'
    my_transfers = [transfer1, transfer2, transfer3]
    write_noxim_table(my_transfers, paths.TRAFFIC_TABLES + table_file_name)