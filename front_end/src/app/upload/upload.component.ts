import { Component } from '@angular/core'
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';

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
    showMessageSuccess: boolean = false;
    messageError: string;
    loading: boolean;
     
    constructor(private chromPackService: ChromPackService,
                private chrompackServiceObservable: ChrompackServiceObservable) { }

    fileChange(event) {
        this.fileList = event.target.files;
    }

    upload(){

        this.messageError = null;
        this.showMessageSuccess = false;

        if(!this._title) {
            this.messageError = 'The title was not informed';
            return;
        }

        if(!this.fileList) {
            this.messageError = 'The file was not selected';
            return;
        }

        this.loading = true;

        this.chromPackService.upload(this._title, this.fileList).subscribe(
            data => {
                this.showMessageSuccess = true;
                this.loading = false;
                this.chrompackServiceObservable.sendRefreshResult();
            },
            errorObj => { 
                this.loading = false;
                this.messageError = errorObj.error;
            }
        );

    }
}