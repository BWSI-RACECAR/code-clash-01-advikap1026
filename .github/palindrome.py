class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
            #type s: string
            #return type: boolean
            
            #TODO: Write code below to return a boolean value with the solution to the prompt.
            bool = True  
            if s.len <= 6:
                 bool = False 
            count = 0 
            length = s.len/2
            for i in range (length) :
                if s[count] != s[-count]:
                     bool = False 
                count = count +1

            if bool == False:
                 return False
            else:
                 return True
            pass

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()