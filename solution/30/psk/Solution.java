package _03_Ç¥ÆíÁý;

import java.util.*;

class Node{
    
    int id;
    Node left;
    Node right;
    
    public Node(int id){
        this.id=id;
    }
    
    @Override
    public String toString(){
        int left_id = (this.left==null?-1:this.left.id);
        int right_id = (this.right==null?-1:this.right.id);
        return "[ id : "+this.id+", left : "+left_id+
            ", right : "+right_id+"]";
    }
    
}

class Solution {
    public String solution(int n, int k, String[] cmd) {
        String answer = "";
        
        Node[] nodes = new Node[n];
        char is[]=new char[n];
        
        for(int i=0;i<n-1;i++){
            if(i==0){
                nodes[i] = new Node(i);
                is[i]='O';
            }
            Node node = nodes[i];
            nodes[i+1] = new Node(i+1);
            Node next = nodes[i+1];
            node.right = next;
            next.left = node;
            nodes[i]=node;
            nodes[i+1]=next;
           is[i+1]='O';
        }
       
        Stack<Node> stack = new Stack<>();
        Node point_node;
        for(String c : cmd){
            String input[]=c.split(" ");
            int cnt=input.length==2?Integer.parseInt(input[1]):-1;
            point_node = nodes[k];
            switch(input[0]){
                case "U","D"->{
                    for(int i=0;i<cnt;i++){
                        point_node = input[0].equals("U")?point_node.left:point_node.right;
                         k=point_node.id;
                    }
                    
                }
                case "C"->{
                    Node left_node = point_node.left;
                    Node right_node = point_node.right;
                    stack.add(point_node);
                    int del_id = point_node.id;
                    nodes[del_id] = null;
                    is[del_id]='X';
                    if(left_node!=null){
                        left_node.right = right_node;
                    }
                    if(right_node!=null){
                        right_node.left = left_node;
                        k = right_node.id;
                    }else if(right_node==null){
                        k = left_node.id;
                    }
                    
                }
                case "Z"->{
                    Node z_node = stack.pop();
                    int z_node_id = z_node.id;
                    nodes[z_node_id]=z_node;
                    is[z_node_id]='O';
                    Node left = z_node.left;
                    Node right = z_node.right;
                    if(left!=null){
                        left.right = z_node;
                    }
                    if(right!=null){
                        right.left = z_node;
                    }
                    
                }
                
            }
        }
        
        // StringBuilder sb =  new StringBuilder();
        // for(int i=0;i<nodes.length;i++){
        //     if(nodes[i]==null)
        //         sb.append("X");
        //     else
        //         sb.append("O");
        // }
        
        // return sb.toString();
        return new String(is);
    }
}
