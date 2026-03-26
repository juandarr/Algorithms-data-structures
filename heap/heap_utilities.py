def show_table(heap) -> None:
    """
    Shows a table of element in the heap following the structure
    Node, Parent, Left child and Right child as colmuns
    """
    print("Node  Parent  Left  Right")
    for idx, i in enumerate(heap.nodes):
        p, l, r = (heap._parent(idx), heap._left(idx), heap._right(idx))
        n = len(heap.nodes)
        i_str = str(heap._check_retrieve_key(i))
        i_str = i_str+' '*(6-len(i_str))
        p_str = str(heap._get_key(p) if p < n and p >= 0 else None)
        p_str = p_str+' '*(8-len(p_str))
        l_str = str(heap._get_key(l) if l < n else None)
        l_str = l_str+' '*(6-len(l_str))
        r_str = str(heap._get_key(r) if r < n else None)
        r_str = r_str+' '*(5-len(r_str))
        print(i_str+p_str+l_str+r_str)