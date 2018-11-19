import { Component } from '@angular/core'
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';import { AlertsService } from '../services/alerts.service';


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
    loading: boolean;
         
    constructor(private chromPackService: ChromPackService,
                private alerts: AlertsService,
                private chrompackServiceObservable: ChrompackServiceObservable,
                public activeModal: NgbActiveModal) { }

    fileChange(event) {
        this.fileList = event.target.files;
    }

    close() {
        this.activeModal.close();
    }

    submit() {

        if (!this._title) {
            this.alerts.error('The title was not informed');
            return;
        }

        if (!this.fileList) {
            this.alerts.error('The file was not selected');
            return;
        }

        this.upload();
    }

    upload() {
        this.loading = true;

        this.chromPackService.upload(this._title, this.fileList).subscribe(
            () => {
                this.alerts.success("Chrompack uploaded with succes");
                this.loading = false;
                this.chrompackServiceObservable.sendRefreshResult();
            },
            err => { 
                this.alerts.error("Error to upload chrompack", err);
                this.loading = false;
            }
        );
    }
}