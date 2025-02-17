package leetcode.metods;

public class L2469_ConvertTheTemperature {

	public double[] convertTemperature(double celsius) {
		double kelvin = celsius + 273.15;
		double fahrenheit = celsius * 1.80 + 32;
		double[] result = { kelvin, fahrenheit };
		return result;
	}

}
