import java.util.*;

https://programmers.co.kr/learn/courses/30/lessons/42586

public class Function {
	int[] prograss;
	int[] speeds;
	int[] result;
	int day;
	int num;
	int resultnum;
	
	public Function(int[] prograss, int[] speeds) {
		this.prograss = prograss;
		this.speeds = speeds;
	}
	
	void addQueue(Queue<Integer> prograssQueue) {
		int length = prograss.length;
		for(int i=0;i<length;i++) {
			prograssQueue.offer(prograss[i]);			
		}
	}
    
	void queuePolling(Queue<Integer> prograssQueue) {
        int[] tempresult = new int[100];
		while(!prograssQueue.isEmpty()) {
			if(prograssQueue.peek()+(day*speeds[num])>=100) {
				prograssQueue.poll();
				num++;
                tempresult[resultnum]++;
				if(!prograssQueue.isEmpty()&&prograssQueue.peek()+(day*speeds[num])<100) {
					resultnum++;
				}
			}
			else {
				day++;
			}
		}
        result = new int[resultnum+1];
	result = Arrays.copyOf(tempresult, resultnum+1);
	}
	
	int[] getResult() {
		return result;
	}
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Function f = new Function(progresses, speeds);
	Queue<Integer> prograssQueue = new LinkedList<Integer>();
	f.addQueue(prograssQueue);
	f.queuePolling(prograssQueue);
        return f.getResult();
    }
}
