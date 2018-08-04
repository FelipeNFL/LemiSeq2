import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Subject } from 'rxjs/Subject';

@Injectable()
export class ChrompackServiceObservable {

    private refreshChrompacks = new Subject<any>();

    constructor() { }

    getRefreshResult(): Observable<any> {
        return this.refreshChrompacks.asObservable();
    }

    sendRefreshResult() {
        this.refreshChrompacks.next();
    }

}
