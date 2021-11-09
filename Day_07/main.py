def get_bottom():
    parent_programs = [x.split() for x in lines if '->' in x]
    children = ' '.join([' '.join(' '.join(x[3:]).split(', ')) for x in parent_programs]).split(' ')
    return [x[0] for x in parent_programs if x[0] not in children][0]


def get_result1():
    return get_bottom()


def get_top():
    parent_programs = [x.split() for x in lines if '->' in x]
    parents = [x[0] for x in parent_programs]
    programs = [x.split()[0] for x in lines]
    top = [x for x in programs if x not in parents]
    return top


def get_parent(child):
    return [x.split()[0] for x in lines if '->' in x and child in ' '.join(x.split()[3:]).split(', ')][0]


def get_siblings(child):
    return [' '.join(x.split()[3:]).split(', ') for x in lines if '->' in x and child in ' '.join(x.split()[3:]).split(', ')][0]


def get_children(parent):
    return [' '.join(x.split()[3:]).split(', ') for x in lines if '->' in x and x.split()[0] == parent][0]


def get_weight(parent, include_children=True):
    program = [x for x in lines if x.split()[0] == parent][0]
    weight = int(program.split()[1][1:-1])
    if include_children:
        if '->' in program:
            children = [x for x in ' '.join(program.split()[3:]).split(', ')]
            for child in children:
                weight += get_weight(child)
    return weight


def all_equal(li):
    for x in li:
        if x != min(li):
            return False
    return True


def wrong_idx(li):
    for x in li:
        if x != min(li):
            return li.index(x)
    return -1


def recursive(children):
    parents = []
    for child in children:
        # Try in case the child has not parent
        #   This is the case if the input is not valid, it means we have reached bottom
        try:
            siblings = get_siblings(child)
            weights = list(map(get_weight, siblings))
            # Check if all weights from siblings are equal
            if not all_equal(weights):
                idx = wrong_idx(weights)
                # Identify the sibling with a wrong weight
                wrong_sibling = siblings[idx]
                children_wrong_sibling = get_children(wrong_sibling)
                children_weights = map(get_weight, children_wrong_sibling)
                # Check if all children from wrong sibling have same weight
                #  If not we will pass this sibling, because the weight of one of the children needs to be adjusted
                if all_equal(children_weights):
                    return get_weight(wrong_sibling, False) - max(weights) + min(weights)
            # Add parent to list for the recursive call
            parent = get_parent(child)
            parents.append(parent)
        except:
            pass
    # Remove duplicates
    parents = list(set(parents))
    # We have reached bottom, so no solution
    if len(parents) == 0:
        return -1
    return recursive(parents)


# This only works if the wrong program has a bigger weight than its siblings
def get_result2():
    children = get_top()
    return recursive(children)


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
