import dropbox

class TransferData(object):
    def __init__(self,access_token):
        self.access_token=access_token

    def uploadFiles(self,file_from,file_to):
        # parameter should contain only access tokens
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb')as f:
            # rb= read binary becos files r stored as bits
            # dbx.files_upload over here files_upload is predefined

            dbx.files_upload(f.read(),file_to,)

def main():
        access_token="sl.AyHUO-rqzvodFsJckSsZJWv6MuR8265UjvP-zaq5WJaSl-LUOt-NW2r-8_ZfTPWWHmw8N2a6KFfQNdZABA_KNv5H1Ag_M-bk6-wQ4p6eCyR4Ek2k0Qq_cIqEXm6-sguQDs6DmH8"
        transferData=TransferData(access_token)

        file_from="text2.txt"
        file_to="/backup/text2.txt"

        transferData.uploadFiles(file_from,file_to)

main()
