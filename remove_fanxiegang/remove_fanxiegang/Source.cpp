#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
	string wavDataIndex = "wavnameList.txt";
	ifstream fileIndex(wavDataIndex.c_str());
	string wavSongName;
	static int totalWavSong = 0;//wav�ļ���
	//string SongName = "waveFile\\year2003\\person00002\\00041.wav";
	//�ڻ���ϵͳ�е�wavname��ϵͳ����\\��д����ʱ�ǵ�б��

	ofstream wavSongNametemp("newNameList.txt", ofstream::app);
	while (fileIndex >> wavSongName)
	{
		totalWavSong++;
		//ȥ������б�ܣ��Ա��ȡ�Դ�������txt
		wavSongName.erase(wavSongName.find("\\"), 1);
		wavSongName.erase(wavSongName.find("\\"), 1);
		wavSongName.erase(wavSongName.find("\\"), 1);
		
		wavSongNametemp << wavSongName << endl;
	}
	wavSongNametemp.close();
	cout << totalWavSong;
	system("Pause");
	return 0;
}


