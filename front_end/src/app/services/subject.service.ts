import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable()
export class SubjectService {

    constructor(private http: HttpClient) { }

    public getMatrixAll(id: String): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${id}/subject/matrix/all`);
    }

    public getMatrixDefault(): any {
        return this.http.get(`${environment.bioprocess_api}/subject/matrix/default`);
    }

}