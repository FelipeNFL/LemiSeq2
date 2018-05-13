import { Component } from '@angular/core'

@Component({
    selector: 'upload',
    templateUrl: './upload.component.html',
    styleUrls: [
        './upload.component.css'
    ]
})
export class UploadComponent {
    
    _title: any;
    _file: any;

    onSubmit(){
        console.log(this._title);
        console.log(this._file);
    }
}