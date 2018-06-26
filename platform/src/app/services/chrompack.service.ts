import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { RequestOptions, Headers } from '@angular/http';
import { environment } from '../../environments/environment';

@Injectable()
export class ChromPackService {

    constructor(private http: HttpClient) { }

    upload(title, fileList): any{
        let file: File = fileList[0];
        let formData: FormData = new FormData();

        formData.append('file', file, file.name);
        formData.append('title', title)

        let headers = new HttpHeaders();

        headers.append('Content-Type', 'multipart/form-data');
        headers.append('Accept', 'application/json');

        return this.http.post(`${environment.bioprocess_api}/chrompack`, formData, {headers: headers})

    }

}