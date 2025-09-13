package lab1;

import java.util.Scanner;

public class Main {
    private static int indexPosition = 0;
    private static Scanner scanner = new Scanner(System.in);

    private static double get_console_input(String[] args, String prompt){
        double number = 0;
        boolean validInput = false;

        if ((args.length - indexPosition) > 0) {
            validInput = true;
            try {
                number = Double.parseDouble(args[indexPosition]);
            } catch (NumberFormatException e) {
                number = getDoubleFromConsole(prompt);
            }
            ++indexPosition;
        }

        if (!validInput) {
            number = getDoubleFromConsole(prompt);
        }

        return number;
    }

    private static double getDoubleFromConsole(String prompt) {
        double result = 0;
        boolean inputValid = false;

        while (!inputValid) {
            try {
                inputValid = true;
                System.out.print("Введите коэффициент "+prompt+": ");
                String input = scanner.nextLine();

                if (input.isEmpty()) {
                    System.out.println("Ошибка: ввод не может быть пустым. Попробуйте снова.");
                    continue;
                }

                result = Double.parseDouble(input);

            } catch (NumberFormatException e) {
                System.out.println("Ошибка: введите корректное число (например: 123.45, -67.8)");
            }
        }

        return result;
    }

    public static void main(String[] args) {
        double coefficientA = get_console_input(args, "A");
        double coefficientB = get_console_input(args, "B");
        double coefficientC = get_console_input(args, "C");

        Biquadrate_equation myEquation = new Biquadrate_equation(coefficientA,coefficientB,coefficientC);
        myEquation.getRootsBikv();
        myEquation.printRoots();

        if (scanner != null){
            scanner.close();
        }
    }
}
