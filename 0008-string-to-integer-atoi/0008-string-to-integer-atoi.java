class Solution {
    public int myAtoi(String s) {
        int i = 0;
        int n = s.length();
        int sign = 1;
        long result = 0;
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        if (i < n && s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (i < n && s.charAt(i) == '+') {
            i++;
        }

        while (i < n && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            int digit = s.charAt(i) - '0';

            result = result * 10 + digit;
            if (sign * result <= Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }

            if (sign * result >= Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }

            i++;
        }

        return (int) (sign * result);
    }
}