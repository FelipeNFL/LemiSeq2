import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable()
export class SubjectService {

    constructor(private http: HttpClient) { }

    public getMatrixAll(id: String): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${id}/subject/matrix`);
    }

    public getMatrixDefault(): any {
        return this.http.get(`${environment.bioprocess_api}/subject/matrix/default`);
    }

    public newSubject(idChrompack: string, name: string): any {
        return this.http.post(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}`, {});
    }

    public getList(idChrompack: string): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject`);
    }

    public delete(idChrompack: string, name: string): any {
        return this.http.delete(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}`, {});
    }

    public addSubjectToSlot(subject: string, slot: string, idChrompack: string): any {
        return this.http.put(`${environment.bioprocess_api}/chrompack/${idChrompack}/slot/${slot}/subject/${subject}`, {});
    }

    public cleanSlot(slot: string, idChrompack: string): any {
        return this.http.delete(`${environment.bioprocess_api}/chrompack/${idChrompack}/slot/${slot}/subject`);
    }

    public build(idChrompack: string, name: string): any {
        return this.http.post(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}/build`, {});
    }

    public isBuilt(idChrompack: string, name: string): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}/build`, {});
    }

    public downloadFiles(idChrompack: string, name: string): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}/build/download`, {responseType: 'blob'});
    }

    public getContigs(idChrompack: string, name: string): any {
        return this.http.get(`${environment.bioprocess_api}/chrompack/${idChrompack}/subject/${name}/build/contigs`, {});
    }
}