import { Component, Input } from '@angular/core'
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SubjectService } from '../services/subject.service';
import { AlertsService } from '../services/alerts.service';


@Component({
    selector: 'new-subject',
    templateUrl: './new-subject.component.html',
    styleUrls: [
        './new-subject.component.css'
    ]
})
export class NewSubjectComponent {
    
    @Input() idChrompack: string;
    _title: any;
    loading: boolean;
         
    constructor(public activeModal: NgbActiveModal,
                private alerts: AlertsService,
                private subjectService: SubjectService,
                private chrompackServiceObservable: ChrompackServiceObservable) { }

    close() {
        this.activeModal.close();
    }

    submit() {

        if (!this._title) {
            this.alerts.error('The title was not informed');
            return;
        }

        this.loading = true;

        this.subjectService.newSubject(this.idChrompack, this._title).subscribe(
            () => {
                this.alerts.success('Subject registered!');
                this.loading = false;
                this.chrompackServiceObservable.sendRefreshResult();
                this.close();
            },
            err => {
                this.loading = false;
                this.alerts.error('There are error to create new subject. Contact the administrator!', err);
            }
        );
    }
}