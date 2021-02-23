# Project Description
* Write an HTML parser that supports the following
	* HTML tags and their attributes: html, head, title, body, p, b, u, i, ol, ul, li, h1, h2, blockquote, div, code, pre, span, iframe (including its src, width, and height attributes)
* Build a tree: your parser must build a tree representing the DOM tree of the html document.
* Java classes: use your own tree implementation, but you may use any/all methods in Java’s String, StringTokenizer, and java.util.Regex
* Provide three public methods:
	* breadthFirst(): prints out the tag name and attributes of each node in the tree in breadth first order
	* preOrder(): prints out the tag name and attributes of each node in the tree in the order of a preorder traversal
	* parse(String): passes a new html document as a string to parse, and any subsequent calls to the other

* Unique IDs: every node must have a string attribute called “id”. If there is one defined in the input (example: <p id=“myPara”>), use it.  Otherwise, generate a unique id for the node, making sure that the id is not used on any other node.
* Text: Even though there is no “text” tag in html, text that appears inside a tag should be its own node in the tree, with the tag name “text”, its own id, and a “content” attribute
	* Example: <P>Hello!</p> would create 2 nodes – a parent node with tag name “p”, and a child node with tag name “text” with an attribute called “content” whose value is “Hello!”
