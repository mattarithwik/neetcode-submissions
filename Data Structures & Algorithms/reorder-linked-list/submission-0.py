class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Phase 1: Locate the exact split boundary (Middle Node)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Phase 2: Disconnect the lists and Reverse the second half
        second_half = slow.next
        slow.next = None  # Sever the connection to terminate the first half
        
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Phase 3: Alternating Zipper Merge (Interleave nodes in-place)
        first_half = head
        second_half = prev  # 'prev' now holds the head of the reversed second half
        
        while second_half:
            # Step A: Cache upcoming steps to prevent pointer evaporation
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            # Step B: Weave the cross-links
            first_half.next = second_half
            second_half.next = tmp1
            
            # Step C: Advance execution tracking pointers forward
            first_half = tmp1
            second_half = tmp2