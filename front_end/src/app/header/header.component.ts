import { Component, Input } from '@angular/core'
import { AuthService } from '../services/auth.service';
import { Subscription } from 'rxjs/Subscription';

@Component({
    selector: 'header',
    templateUrl: './header.component.html',
    styleUrls: [
        './header.component.css'
    ]
})

export class HeaderComponent {

    refreshLogout: Subscription;
    isLogged: boolean;

    constructor(private authService: AuthService) { }

    ngOnInit() {
        this.isLogged = this.authService.isLogged();

        this.refreshLogout = this.authService.refreshLogin().subscribe(statusLogin => {
            this.isLogged = statusLogin;
        });
    }
}