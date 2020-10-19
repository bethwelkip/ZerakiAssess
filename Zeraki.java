/* *****************************************************************************
 *  Name:    Bethwel Kiplimo
 *
 *  Description:  The class contains my responses to Zeraki's programming
 * assessment questions.
 **************************************************************************** */

import java.util.Arrays;

public class Zeraki {

    // Reverses the String as specified in the second prompt of the evaluation
    // no assumptions made.
    public static String reverseString(String s) {
        char[] y = s.toCharArray();
        int i = 0;
        while (i < y.length) {
            int currentIndex = i + Math.min(3, y.length - i - 1);
            int shift = (Math.min(3, y.length - i - 1) + 1) / 2;
            while (currentIndex > i) {
                char temp = y[i];
                y[i] = y[currentIndex];
                y[currentIndex] = temp;
                currentIndex--;
                i++;
            }
            i = i + shift;
        }

        return new String(y);
    }

    /* Returns the missing integer as specified in  first prompt
    time complexity: 0(NlgN)- due to sorting. could achieve 0(N) time
    complexity using hashtables with would be 0(N) time and 0(N) space.
     */
    private static int missingInt(int[] ints) {
        Arrays.sort(ints);
        int n = ints.length;
        int missing = 0;
        for (int i = 0; i < n; i++) {
            if (ints[i] != i + 1) {
                missing = i + 1;
                break;
            }
        }
        return missing;
    }


    public static void main(String[] args) {
        System.out.println(reverseString(" Tempor ip"));
        int[] sints = new int[4];
        sints[0] = 3;
        sints[1] = Integer.parseInt("5");
        sints[2] = 4;
        sints[3] = 1;
        System.out.println(missingInt(sints));
    }
}
