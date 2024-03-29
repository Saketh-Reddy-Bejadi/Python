
// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;

class Upscaling {
    static void print(char[] arr) {
        for (char i : arr) {
            System.out.print(i);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        while (a-- > 0) {
            int b = sc.nextInt();
            b = b * 2;
            char[] arr = new char[b];
            char[] arr2 = new char[b];
            int i = 0, j = 0;
            boolean s1 = true, s2 = false;
            while (i < b) {
                if (s1) {
                    arr[i++] = '#';
                    arr[i++] = '#';
                    arr2[j++] = '.';
                    arr2[j++] = '.';
                    s2 = true;
                    s1 = false;
                    continue;
                }
                if (s2) {
                    arr[i++] = '.';
                    arr[i++] = '.';
                    arr2[j++] = '#';
                    arr2[j++] = '#';
                    s1 = true;
                    s2 = false;
                    continue;
                }
            }

            i = 0;b=b/2;
            while (i < b) {
                if (i % 2 != 0) {
                    print(arr2);
                    print(arr2);
                } else {
                    print(arr);
                    print(arr);
                }
                i++;
            }

        }
        sc.close();
    }
}