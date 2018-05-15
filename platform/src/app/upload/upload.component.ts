import { Component } from '@angular/core'
import { ChromPackService } from '../../services/chrompack.service';
import 

@Component({
    selector: 'upload',
    templateUrl: './upload.component.html',
    styleUrls: [
        './upload.component.css'
    ]
})
export class UploadComponent {
    
    _title: any;
    fileList: FileList;
    showMessageError: boolean = false;
    showMessageSuccess: boolean = false;
    messageError: string;
     
    constructor(private chromPackService: ChromPackService) { }

    fileChange(event) {
        this.fileList = event.target.files;
    }

    upload(){

        if(this._title == null) {
            this.showMessageError = true;
            this.messageError = 'The title was not informed';
            return;
        }

        if(this.fileList == null) {
            this.showMessageError = true;
            this.messageError = 'The file was not selected';
            return;
        }

        this.chromPackService.upload(this._title, this.fileList);
    }
}