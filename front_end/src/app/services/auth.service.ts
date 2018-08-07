import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";
import { Router } from "@angular/router";
import { Observable } from "rxjs/Observable";
import { Subject } from "rxjs/Subject";

@Injectable()
export class AuthService {

    emitRefreshLogin = new Subject<any>();

    constructor(private http: HttpClient,
                private router: Router) { }

    public requestToken(email: string, password: string): any {
        return this.http.post(`${environment.auth_api}/token`, {username: email, password})
    }

    public setSession(token: string, fullname: string) {
        localStorage.setItem('token', token);
        localStorage.setItem('fullname', fullname);
        this.emitRefreshLogin.next(true);
    }

    public getFullname() {
        return localStorage.getItem('fullname');
    }

    public logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('fullname');
        this.router.navigateByUrl('/login');
        this.emitRefreshLogin.next(false);
    }

    public isLogged() {
        return Boolean(localStorage.getItem('token'));
    }

    public refreshLogin(): Observable<any> {
        return this.emitRefreshLogin.asObservable();
    }
}
