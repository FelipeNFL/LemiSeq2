import { Injectable, Injector, Inject } from '@angular/core';

import { environment } from '../environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { RequestOptions, Headers } from '@angular/http';

@Injectable()
export class ChromPackService {

    constructor(private http: HttpClient) { }

    upload(title, fileList){
        let file: File = fileList[0];
        let formData: FormData = new FormData();
        formData.append('file', file, file.name);
        formData.append('title', title)
        let headers = new HttpHeaders();
        /** In Angular 5, including the header Content-Type can invalidate your request */
        headers.append('Content-Type', 'multipart/form-data');
        headers.append('Accept', 'application/json');
        this.http.post(`${environment.bioprocess_api}/chrompack`, formData, {headers: headers})
            .subscribe(
                data => console.log('success'),
                error => console.log(error)
            )
    }

}