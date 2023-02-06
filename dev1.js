

Your Question:How can I remove a specific item from an array?
Your Answer:-

You can use the JavaScript array method .splice() to remove a specific item from an array. The .splice() method takes two parameters: the index of the item you want to remove, and the number of items you want to remove.

For example, if you have an array like this:

let arr = [1, 2, 3, 4, 5];

And you want to remove the item at index 2 (3 in this case), you can use the .splice() method like this:

arr.splice(2, 1);

This will remove the item at index 2 (3 in this case) and return it. The resulting array will be:

[1, 2, 4, 5]