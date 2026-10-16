/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int count = 0;
    int result = 0;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    private boolean inorder(TreeNode root, int k) {
        if (root == null) {
            return false;
        }

        if (inorder(root.left, k)) {
            return true;
        }

        count++;

        if (count == k) {
            result = root.val;
            return true;
        }

        return inorder(root.right, k);
    }
}
