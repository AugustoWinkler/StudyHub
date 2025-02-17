package leetcode.metods;

import java.util.ArrayList;
import java.util.List;

public class L0349_IntersectionOfTwoArrays {

	static public int[] intersection(int[] nums1, int[] nums2) {
		List<Integer> result = new ArrayList<>();
		List<Integer> array1 = new ArrayList<>();
		List<Integer> array2 = new ArrayList<>();
		for (int num : nums1) {
			array1.add(num);
		}
		for (int num : nums2) {
			array2.add(num);
		}
		for (int num : array1) {
			if (array2.contains(num) && result.contains(num) == false) {
				result.add(num);
			}
		}

		int[] resultArray = new int[result.size()];
		for (int i = 0; i <= result.size() - 1; i++) {
			resultArray[i] = result.get(i);
		}
		return resultArray;
	}
}
