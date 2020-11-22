// 最简单粗暴

class MyHashSet {
    private int[] arr;

    /** Initialize your data structure here. */
    public MyHashSet() {
        arr = new int[1000001];
    }
    
    public void add(int key) {
        arr[key] = 1;
    }
    
    public void remove(int key) {
        arr[key] = 0;
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return arr[key] == 1;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */


 // 在每一个位置上建立LinkedList
 