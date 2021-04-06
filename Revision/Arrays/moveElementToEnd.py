def moveElementToEnd(array, toMove):
    # Write your code here.
    insertAtPosition = 0
    i = 0
    while i < len(array):
    	if array[i] != toMove:
    		elementAtCurremt = array[i]
    		elementAtInsert = array[insertAtPosition]
    		array[insertAtPosition], array[i] = elementAtCurremt, elementAtInsert
    		insertAtPosition += 1
    	i += 1
    return array
