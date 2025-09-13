package lab1;

import java.util.ArrayList;
import java.util.List;

public class Biquadrate_equation {
    private double coefA;
    private double coefB;
    private double coefC;
    private List<Double> rootsList = new ArrayList<>();

    public Biquadrate_equation(double coefA, double coefB, double coefC){
        this.coefA=coefA;
        this.coefB=coefB;
        this.coefC=coefC;
    }

    private List<Double> getSimpleKvRoots(double coefficient) {
        List<Double> result = new ArrayList<>();
        if (coefficient > 0) {
            result.add(Math.sqrt(coefficient));
            result.add(-Math.sqrt(coefficient));
        } else if (coefficient == 0) {
            result.add(0.0);
        }
        return result;
    }

    public void getRootsBikv() {
        double d = coefB * coefB - 4 * coefA * coefC;

        if (d == 0.0) {
            double bikvRoot = -coefB / (2.0 * coefA);
            rootsList.addAll(getSimpleKvRoots(bikvRoot));
        } else if (d > 0.0) {
            double sqD = Math.sqrt(d);
            double bikvRoot1 = (-coefB + sqD) / (2.0 * coefA);
            double bikvRoot2 = (-coefB - sqD) / (2.0 * coefA);
            rootsList.addAll(getSimpleKvRoots(bikvRoot1));
            rootsList.addAll(getSimpleKvRoots(bikvRoot2));
        }
    }

    public void printRoots() {
        int lenRoots = rootsList.size();
        if (lenRoots == 0) {
            System.out.println("Нет корней");
            return;
        }

        System.out.println("Корней " + lenRoots + ".");
        for (int i = 0; i < lenRoots; i++) {
            System.out.printf("Корень номер %d равен %.4f%n", i + 1, rootsList.get(i));
        }
    }
}
