import java.util.Scanner;

public class Main {
    static Scanner scn = new Scanner(System.in);
    
    public void main() {

    }
    
    private static int enterChoice() {
        System.out.print("\n1 - View an entry\n2 - Update an entry\n3 - Add an entry\n4 - Delete an entry\n5 - End the program")
        return scn.nextInt();
    }

    private static String getMovieID(String title) {
        return "test";
    }

    private static int getMovieYear(String id) {
        return 0;
    }

    private static String getMovieGenre(String id) {
        return "test";
    }

    private static String getMovieLanguage(String id) {
        return "test";
    }

    private static int getMovieRating(String id) {
        return 0;
    }

    private static String getMovieTitle(String id) {
        return "test";
    }
}