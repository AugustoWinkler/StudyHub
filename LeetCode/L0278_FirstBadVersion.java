package leetcode.metods;

public class L0278_FirstBadVersion {

	public int firstBadVersion(int n) {
		int low = 1;
		int high = n;
		while (low < high) {
			int mid = low + (high - low) / 2;
			if (isBadVersion(mid)) {
				high = mid;
			} else {
				low = mid + 1;
			}
		}
		return low;
	}

	private boolean isBadVersion(int mid) {
		// REMOVE ERROR
		return false;
	}
}
