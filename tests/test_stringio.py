import os
import sys
import pyexcel
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import BytesIO as StringIO
from base import create_sample_file1


class TestStringIO:

    def test_xls_stringio(self):
        xlsfile = "cute.xls"
        create_sample_file1(xlsfile)
        with open(xlsfile, "rb") as f:
            content = f.read()
            r = pyexcel.get_sheet(file_type="xls", file_content=content)
            result=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1.1, 1]
            actual = pyexcel.utils.to_array(r.enumerate())
            assert result == actual
        if os.path.exists(xlsfile):
            os.unlink(xlsfile)


    def test_xls_output_stringio(self):
        data = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        io = pyexcel.save_as(dest_file_type="xls",
                             array=data)
        r = pyexcel.get_sheet(file_type="xls", file_content=io.getvalue())
        result=[1, 2, 3, 4, 5, 6]
        actual = pyexcel.utils.to_array(r.enumerate())
        assert result == actual