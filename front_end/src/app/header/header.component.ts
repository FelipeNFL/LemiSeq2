import { Component, Input } from '@angular/core'
import { AuthService } from '../services/auth.service';
import { Subscription } from 'rxjs/Subscription';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';

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

    constructor(private authService: AuthService,
                private modalService: NgbModal) { }

    ngOnInit() {
        this.isLogged = this.authService.isLogged();

        this.refreshLogout = this.authService.refreshLogin().subscribe(statusLogin => {
            this.isLogged = statusLogin;
        });
    }

    openUploadModal() {
        this.modalService.open(UploadComponent);
    }
}