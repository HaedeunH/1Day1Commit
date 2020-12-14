import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/12921#
// ko.wikipedia.org/wiki/에라토스테네스의_체
// 동적배열 ArrayList 이용시 효율성 테스트 통과못함

class Solution {
    public int solution(int n) {
        int answer = 0;
		boolean[] primeList = new boolean[1000001];
		for(int i=2;i<=n;i++) {
			primeList[i] = true;
		}
		for(int i=2;(i*i)<=n;i++) {
			if(primeList[i]) {
				for(int j=i*i; j<=n; j+=i) {
					primeList[j] = false;
				}
			}
		}
		for(int i=2;i<=n;i++) {
			if(primeList[i]) {
				answer++;
			}
		}
        return answer;
    }
}
