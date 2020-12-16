import java.util.*;

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

	void newResult(Queue<Integer> prograssQueue) {
		while(!prograssQueue.isEmpty()) {
			if(prograssQueue.peek()+(day*speeds[num])>=100) {
				prograssQueue.poll();
				num++;
				if(!prograssQueue.isEmpty()&&prograssQueue.peek()+(day*speeds[num])<100) {
					resultnum++;
				}
			}
			else {
				day++;
			}
		}
		result = new int[resultnum+1];
	}
	
	void queuePolling(Queue<Integer> prograssQueue) {
		int resultnum = 0;
		int num = 0;
		int day = 0;
		while(!prograssQueue.isEmpty()) {
			if(prograssQueue.peek()+(day*speeds[num])>=100) {
				prograssQueue.poll();
				num++;
				result[resultnum]++;
				if(!prograssQueue.isEmpty()&&prograssQueue.peek()+(day*speeds[num])<100) {
					resultnum++;
				}
			}
			else {
				day++;
			}
		}
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
		f.newResult(prograssQueue);
		f.addQueue(prograssQueue);
		f.queuePolling(prograssQueue);
        return f.getResult();
    }
}