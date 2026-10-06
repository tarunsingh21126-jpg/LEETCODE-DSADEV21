class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int totalsum = 0;
        for (int i= 0;i<n;i++){
            totalsum+=cardPoints[i];
        }
        int windowsize = n -k;
        if(windowsize == 0){
            return totalsum;
        }
        int windowsum = 0;
        for(int i = 0;i< windowsize;i++){
            windowsum+=cardPoints[i];
        }
        int minsum  = windowsum;
        for(int i= windowsize;i<n;i++){
            windowsum+=cardPoints[i];
            windowsum -=cardPoints[i -windowsize];
            minsum  = Math.min(minsum,windowsum);
        }
        return totalsum - minsum;
    }
}