class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Zähler für die Anzahl der Elemente, die nicht gleich val sind

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) { // Wenn das aktuelle Element nicht gleich val ist
                nums[k] = nums[i]; // Füge es an die k-te Position
                k++; // Erhöhe den Zähler
            }
        }

        return k; // Gibt die Anzahl der Elemente zurück, die nicht gleich val sind
    }
}
