class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
            #type s: string
            #return type: boolean
            
            #TODO: Write code below to return a boolean value with the solution to the prompt.
            
            return s == s[::-1] and len(s) > 6
      
            pass

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()