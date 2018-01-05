#!/usr/local/bin/python3
"""
Lesson 3 Project 1
"""
import unittest
import tempfile
import shutil
import glob
import os 

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible"
        files = ["this.txt", "that.txt", "the_other.txt"]
        for filename in files:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        found_files = os.listdir(self.dirname)
        self.assertEqual(sorted(files),sorted(found_files),'found is not the same as file')
           
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        "Verify binary file has million bytes"
        expected = 1000000
        f = open("tmp", 'w')
        for i in range(0,expected):
            f.write('a')
        f.close()
        statinfo = os.stat('tmp')
        self.assertTrue(expected == statinfo.st_size,'File size fails')

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()
