def findLCA(root, n1, n2):

    if root.value == n1 or root.value == n2:
        return root

    leftLca = findLCA(root.left, n1, n2)
    rightLca = findLCA(root.right, n1, n2)

    if leftLca and rightLca:
        return root

    return leftLca
