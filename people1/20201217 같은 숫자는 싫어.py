import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        int num=arr.length;
 
        for(int i=1;i<arr.length;i++){
        	
        	if(arr[i-1] != arr[i]) {
        		answer.add(arr[i-1]);
        	}  
        }
        
        answer.add(arr[num-1]);
        int num1=answer.size();
        
        int []answer1=new int[num1];
        for(int i=1; i<num1;i++){
        	answer1[i]=answer.get(i);
        		
        	}

        return arr;
        
        }
        
        
    }
