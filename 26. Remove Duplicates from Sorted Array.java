class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; // Wenn das Array leer ist, gibt es keine einzigartigen Elemente
        }

        int uniqueIndex = 1; // Start bei 1, da das erste Element immer einzigartig ist

        for (int current = 1; current < nums.length; current++) {
            if (nums[current] != nums[current - 1]) { // Wenn das aktuelle Element nicht gleich dem vorherigen ist
                nums[uniqueIndex] = nums[current]; // Füge das einzigartige Element hinzu
                uniqueIndex++; // Erhöhe den Index für das nächste einzigartige Element
            }
        }

        return uniqueIndex; // Gibt die Anzahl der einzigartigen Elemente zurück
    }
}
