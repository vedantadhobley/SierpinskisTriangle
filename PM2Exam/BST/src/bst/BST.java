package bst;

public class BST {

	Node head;
	
	public BST(){
		head = null;
	}
	
	public void add(int data){
		if (head == null){
			head = new Node(data);
			System.out.println("HEAD: " + data);
		} else{
			add(data,head);
		}
	}
	
	public void add(int data, Node ptr){
		
		if (ptr == null){
			ptr = new Node(data);
			System.out.println("ADD " + data);
			return;
		}
		
		if (data < ptr.data){
			System.out.println(data + " LEFT OF " + ptr.data);
			add(data,ptr.left);
		} else{
			System.out.println(data + " RIGHT OF " + ptr.data);
			add(data,ptr.right);
		}
	}
	
}
