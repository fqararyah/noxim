import os

class NocTransfer:
    def __init__(self, src_id, dst_ids, size, start_cycle=100):
        self.src_id = src_id
        # Ensure dst_ids is a list even if a single integer is passed
        self.dst_ids = [dst_ids] if isinstance(dst_ids, int) else dst_ids
        self.size = size
        self.start_cycle = start_cycle

    def generate_table_entries(self):
        entries = []
        num_dsts = len(self.dst_ids)
        # For boradcast:
        # the hub is on one of the nodes, and that is not given in the dst ids
        if num_dsts > 1:
            num_dsts += 1
        
        # Logic: Split the total 'size' across all destinations to 
        # model a single broadcast event rather than N unique copies.
        # We use integer division to keep flit counts whole.
        split_size = max(1, self.size // num_dsts)

        for dst in self.dst_ids:
            # Noxim doesn't like self-traffic (src == dst). 
            # If src is in dst list, we skip it to prevent simulation errors.
            if self.src_id == dst:
                continue
            
            entries.append({
                'src': self.src_id,
                'dst': dst,
                'cycle': self.start_cycle,
                'size': split_size
            })
        return entries